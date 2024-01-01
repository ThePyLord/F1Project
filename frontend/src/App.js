import { filter,  map, range, sample, sampleSize, size, sortBy } from "lodash"
import React, { useEffect, useState } from 'react';
import { csv } from 'd3';
import './App.css';
import { LinePlot, ScatterPlot } from "./utils/Plots";

// Test data
const randomPoints = map(range(-1, 1), (i) => {
  return {
    x: i,
    y:sigmoid(i)
  }
});

function sigmoid(x) {
    return 1 / (1 + Math.exp(-x));
}

const parseDate = (date) => {
    const newDate = new Date(Date(date));
    return `${newDate.getDate()}/${newDate.getMonth()}/${newDate.getFullYear()}`;
}


function App() {
    const [currentTime, setCurrentTime] = useState(0);
    const [circuit, setCircuit] = useState([]);
    const [performance, setPerformance] = useState([]);
    const [tips, setTips] = useState([]);



    useEffect(() => {
        fetch('/time')
            .then(res => res.json())
            .then(data => {
            setCurrentTime(data.time);
        });

        fetch('/circuit')
            .then(res => res.json())
            .then(data => {
            setCircuit(data);
        });

        fetch('/positions/average')
            .then(res => res.json())
            .then(data => {
                const currEra = sortBy(
                    filter(data, (d) => d.year >= 1990 && d.averagePos), 
                    (d) => d.year)
                
                setPerformance(currEra);
            });
        
        return () => {}
    }, []);


    useEffect(() => {
        async function fetchTips(url) {
            const tipsDf = await csv(url)
            tipsDf.forEach((d) => {
                // convert numerical values to numbers
                d.year = +d.year;
                d.passengers = +d.passengers;
            })
            // setTips(tipsDf);
            setTips(filter(tipsDf, {'month': 'May'}));
        }
        fetchTips('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv');
    }, []);

    return (
        <div className="App">
            <header className="banner">
                <h1 className="bannerTitle">Formula 1 Insights</h1>
            </header>
            <main className="main">
                <p>The current time is {currentTime}.</p>
                <p>Here is the current date: {parseDate(currentTime)}</p>
                <p> The current circuit is {circuit.name}, it's in {circuit.country}.</p>
                <div>
                    The following example is a line plot of points from the sample seaborn dataset "flights.csv".
                </div>
                <LinePlot data={tips}
                    x='year'
                    y='passengers'
                    fill={'#4C72B0'}
                    // markers={true}
                    backgroundColor={'rgba(255,255,255,0.27)'}
                />
            </main>
        </div>
    );
}

export default App;
