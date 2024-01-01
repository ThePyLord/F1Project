/**
 * This file contains the code for the plots to be used for visualizations in the frontend.
 * Each component to be created will be a function that returns a type of plot, e.g. a line plot
 * @see LinePlot.
 */

import * as d3 from "d3";
import { extent, line, scaleLinear, select } from "d3";
import { round } from "lodash";
import { useEffect, useMemo, useRef, useState } from "react";
import Axis from "./Axis";

function D3Chart({ data }) {
	const [selection, setSelection] = useState(null);
	const chartRef = useRef();
	const chartWidth = 800;
	const chartHeight = 500;

	useEffect(() => {
		if (!selection) {
			setSelection(select(chartRef.current));
		}

		// D3.js code for creating the visualization
		// ...
		const svg = d3.select(chartRef.current);
		const margin = { top: 20, right: 20, bottom: 30, left: 40 };
		const width = chartWidth - margin.left - margin.right;
		const height = chartHeight - margin.top - margin.bottom;
		// Create scales
		const xScale = d3
			.scaleBand()
			.range([0, width])
			.padding(0.1)
			.domain(data.map((d) => `${d.name}`));
		// Use D3 to bind data and create/update elements
		// ...
		const yScale = d3.scaleLinear()
			.range([height, 0])
			.domain([0, d3.max(data, (d) => d.totalWins)]);


		// Create axes
		const xAxis = d3.axisBottom(xScale);

		const yAxis = d3.axisLeft(yScale);

		// Render axes
		svg
			.append('g')
			.attr('transform', `translate(${margin.left},${height + margin.top})`)
			.call(xAxis)
			.selectAll('text')
			.attr('transform', 'rotate(-45)')
			.style('text-anchor', 'end');


		svg
			.append('g')
			.attr('transform', `translate(0, ${margin.top})`)
			.call(yAxis);

		// Render bars
		svg
			.selectAll('.bar')
			.data(data)
			.enter()
			.append('rect')
			.attr('class', 'bar')
			.attr('x', (d) => xScale(`${d.name}`))
			.attr('y', (d) => yScale(d.totalWins) + margin.top)
			.attr('width', xScale.bandwidth())
			.attr('height', (d) => height - yScale(d.totalWins))
			.attr('fill', 'steelblue');
		// console.log(select(chartRef.current).data(data))
		// Cleanup or remove elements on component unmount
		return () => {
			// Cleanup code here
		};
	}, [data, selection]); // Trigger update when data changes

	return (
		<div>
			<svg ref={chartRef} width={chartWidth} height={chartHeight}>
				{/* Container for D3 visualization */}
			</svg>
		</div>
	);
}

function LinePlot({
	data,
	x,
	y,
	title,
	width = 640,
	height = 400,
	markers = false,
	...props
}) {
	const fill = props.fill || "red";
	const margin = {
		top: 20,
		right: 20,
		bottom: 30,
		left: 60
	}

	const domain = useMemo(() => {
		console.log('computing domain', `${data[x]}`)
		return {
			x: extent(data, (d) => d[x]),
			y: extent(data, (d) => d[y])
		}
	}, [data, x, y])

	const range = {
		x: [margin.left, width],
		y: [height - margin.bottom, margin.top]
	}

	const xScale = scaleLinear()
		.domain(domain.x)
		.range([margin.left, width]);

	const yScale = scaleLinear()
		.domain(domain.y)
		.range([height - margin.bottom, margin.top]);

	const lineGen = line()
		.x((d, i) => xScale(d[x]))
		.y((d) => yScale(d[y]))

	return (
		<svg 
			width={width + margin.left + margin.right} 
			height={height + margin.top + margin.bottom}>
			<path fill="none" stroke={fill} strokeWidth="1.5" d={lineGen(data)} />
			<g fill={fill} stroke="currentColor" strokeWidth="1.5">
				{markers && data.map((d, i) => (
					<circle key={i} cx={xScale(d[x])} cy={yScale(d[y])} r="2.5">
						<title>{`(${round(d[x], 2)}, ${round(d[y], 2)})`}</title>
					</circle>
				))}
			</g>
			<Axis
				domain={domain}
				labels={[x, y]} // labels is intended to be an array of the labels for the axes(x and y)
				range={range}
				margin={margin}
				height={height}
			/>
		</svg>
	);
}

/**
 * Create a scatter plot with D3.js
 * @param width
 * @param height
 * @param data
 */
function ScatterPlot({
	data,
	x,
	y,
	title,
	width = 640,
	height = 400,
	...props
}) {
	const fill = props.fill || "red";
	const margin = {
		top: 20,
		right: 20,
		bottom: 30,
		left: 60
	}
	
	const domain = useMemo(() => {
		return {
			x: extent(data, (d) => d[x]),
			y: extent(data, (d) => d[y])
		}
	}, [data, x, y])

	const range = {
		x: [margin.left, width],
		y: [height - margin.bottom, margin.top]
	}

	const xScale = scaleLinear()
		.domain(domain.x)
		.range([margin.left, width]);

	const yScale = scaleLinear()
		.domain(domain.y)
		.range([height - margin.bottom, margin.top]);


	return (
		<svg
			width={width + margin.left + margin.right}
			height={height + margin.top + margin.bottom}
			style={{ backgroundColor: props.backgroundColor }}
		>
			{
				data.map((d, i) => (
					<circle
						key={i}
						cx={xScale(d[x])}
						cy={yScale(d[y])}
						r="2.5"
						fill={fill}>
							<title
								style={{ fill: "green" }}
							>{`(${round(d[x], 2)}, ${round(d[y], 2)})`}</title>
					</circle>

				))
			}
			<Axis
				domain={domain}
				labels={[x, y]} // labels is intended to be an array of the labels for the axes(x and y)
				range={range}
				margin={margin}
				height={height}
			/>
		</svg>
	)
}


export {
	D3Chart, LinePlot,
	ScatterPlot
};

// const ticks = useMemo(() => {
// 	const xScale = scaleTime()
// 		.domain([d3.min(data, (d) => d[x]), d3.max(data, (d) => d[x])])
// 		.range([0, width - 10]);
// 	// const yScale = d3.scaleLinear()
// 	//     .domain([d3.min(data, (d) => d[1]), d3.max(data, (d) => d[1])])
// 	//     .range([height-10, 0]);
// 	// const widthTicks = 10;
// 	const pixelsPerTick = 50;
// 	const numberOfTicksTarget = Math.max(
// 		1,
// 		Math.floor(width / pixelsPerTick)
// 	);
// 	return xScale
// 		.ticks(numberOfTicksTarget)
// 		.map((value) => ({
// 			value,
// 			xOffset: xScale(value)
// 		}));
// }, [data, width]);
