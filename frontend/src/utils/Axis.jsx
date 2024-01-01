import React, { useMemo } from "react";
import { scaleLinear } from "d3";
import { mean, size } from "lodash";

const labelStyle = {
    fontSize: "0.75em",
    textAnchor: "middle",
    // transform: `translate(${props.width / 2}px, ${props.height}px))`
}


/**
 * Renders an axis component.
 *
 * @param {Object} props - The component props.
 * @param {number[]} props.domain - The domain of the axis.
 * @param {number[]} props.range - The range of the axis.
 * @param {string[]} labels - The x and y axis labels respectively.
 * @param {number} margin - The margin of the axis.
 * @param {number} props.height - The height of the axis.
 * @returns {JSX.Element} The rendered Axis component.
 */
function Axis({
    domain,
    range,
    labels,
    margin,
    ...props
}) {
    const tickOffset = props.height - (props.height / 20)

    const domainRangeKey = useMemo(() => {
        return `${Object.values(domain).join(",")}-${Object.values(range).join(",")}`
    }, [domain, range])

    const ticks = useMemo(() => {
        const xScale = scaleLinear()
            .domain(domain.x)
            .range(range.x)
        const width = Math.abs(range.x[1] - range.x[0])
        const pixPerTick = range.x[1] / xScale.ticks().length
        const numberOfTicksTarget = Math.max(
            1,
            Math.floor(width / pixPerTick)
        )
        return xScale.ticks(numberOfTicksTarget)
            .map(value => ({
                value,
                xOffset: xScale(value)
            }))

    }, [domain.x, range.x])


    const yTicks = useMemo(() => {
        const yScale = scaleLinear()
            .domain(domain.y)
            .range(range.y)

        const height = Math.abs(range.y[1] - range.y[0])
        const pixPerTick = range.y[0] / size(yScale.ticks())
        const numberOfTicksTarget = Math.max(1,Math.floor(height / pixPerTick))
        return yScale.ticks(numberOfTicksTarget)
            .map(value => ({
                value,
                yOffset: yScale(value)
            }))

    }, [domainRangeKey])


    return (
        <>
            {/* y-axis */}
            <path
                d={[
                    "M", margin.left - (margin.left * 0.05), margin.top,
                    "v", tickOffset - margin.top,
                ].join(" ")}
                stroke="currentColor"
                fill="none" />
            {/* y-axis ticks */}
            {
                yTicks
                    .map(({ value, yOffset }) => (
                        <g
                            key={value}
                            transform={`translate(${margin.left - (margin.left * 0.5)}, ${yOffset})`}
                        >
                            <line
                                x1={margin.left - (margin.left * 0.75)}
                                x2={margin.left - (margin.left * 0.55)}
                                stroke="currentColor" />
                            <text
                                key={value}
                                style={{
                                    fontSize: "0.75em",
                                    textAnchor: "middle",
                                    transform: `translate(${margin.left - (margin.left * 0.9)}px, 4px)`
                                }}
                            >
                                {value}
                            </text>
                        </g>
                    ))
            }
            {/* x-axis */}
            <path d={[
                    "M", range.x[0], tickOffset,
                    "v", -6,
                    "H", range.x[1],
                    "v", 6
                ].join(" ")}
                fill="none"
                stroke="currentColor"/>
            {
                ticks
                    .map(({ value, xOffset }) => (
                        <g
                            key={value}
                            transform={`translate(${xOffset}, -6)`}
                        >
                            <line
                                y1={tickOffset}
                                y2={tickOffset + 10}
                                stroke="currentColor" />
                            <text
                                key={value}
                                style={{
                                    fontSize: "0.75em",
                                    textAnchor: "middle",
                                    transform: `translateY(${props.height + 5}px)`
                                }}
                            >
                                {value}
                            </text>
                        </g>
                    ))
            }
            {/*x and y-axis labels respectively*/}
            <text
                x={mean(range.x)}
                y={props.height + 15}
                style={labelStyle}
                >{labels[0]}</text>
            <text
                x={margin.left - (margin.left * 0.7)}
                y={4}
                style={{
                    ...labelStyle,
                    transform: `translate(${margin.left - (margin.left * 0.7)}px,${props.height / 2}px) rotate(-90deg)`
                }}
                >{labels[1]}</text>
        </>
    )
}

export default Axis