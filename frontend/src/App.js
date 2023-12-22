import * as d3 from "d3";
import {select} from "d3-selection";
import React, {useState, useEffect, useRef} from 'react';
import './App.css';

const D3Chart = ({ data }) => {
  const chartRef = useRef();

  useEffect(() => {
    // D3.js code for creating the visualization

    // Use D3 to bind data and create/update elements
    // ...
    select(chartRef.current)
        .data(data)
        .append("rect")
        .attr("width", 100)
        .attr("height", 100)
        .attr('opacity', 0.5)
        .attr("fill", "blue");

    console.log(select(chartRef.current).data(data))
    // Cleanup or remove elements on component unmount
    return () => {
      // Cleanup code here
    };
  }, [data]); // Trigger update when data changes

  return (
      <div>
        <svg ref={chartRef} width={800} height={400}>
            {/* Container for D3 visualization */}
          </svg>
      </div>

);
};


function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [circuit, setCircuit] = useState([]);
  const [performance, setPerformance] = useState([]);
  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });

    fetch('/circuit').then(res => res.json()).then(data => {
      // console.log(data)
      setCircuit(data);
    });

    fetch('/performance').then(res => res.json()).then(data => {
        // console.log(data)
        setPerformance(data);
    });
  }, []);

  const parseDate = (date) => {
    const newDate = new Date(Date(date));
    return `${newDate.getDate()}/${newDate.getMonth()}/${newDate.getFullYear()}`;
  }

  return (
    <div className="App">
      <header className="banner">
          <h1 className="bannerTitle">Formula 1 Insights</h1>
      </header>
      <main className="main">
        <p>The current time is {currentTime}.</p>
        <p>Here is the current date: {parseDate(currentTime)}</p>
        <p> The current circuit is {circuit.name}, it's in {circuit.country}.</p>
        <D3Chart data={performance} />
      </main>
    </div>
  );
}

export default App;
