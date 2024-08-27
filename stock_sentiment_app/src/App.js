// // import logo from './logo.svg';
// // import './App.css';

// // function App() {
// //   return (
// //     <div className="App">
// //       <header className="App-header">
// //         <img src={logo} className="App-logo" alt="logo" />
// //         <p>
// //           Edit <code>src/App.js</code> and save to reload.
// //         </p>
// //         <a
// //           className="App-link"
// //           href="https://reactjs.org"
// //           target="_blank"
// //           rel="noopener noreferrer"
// //         >
// //           Learn React
// //         </a>
// //       </header>
// //     </div>
// //   );
// // }

// // export default App;
// import React, { useEffect, useState } from 'react';

// function News() {
//   const [articles, setArticles] = useState([]);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const tickers = ['AAPL'];
//     const tickerString = tickers.join(',');
//     let start = "2024-01-01"
//     let end = "2024-08-30"
//     // Fetch the data from Flask API
//     fetch(`http://127.0.0.1:5000/api/news?tickers=${tickerString}&start=${start}&end=${end}`)
//       .then(response => {
//         if (!response.ok) {
//           throw new Error('Network response was not ok');
//         }
//         return response.json();
//       })
//       .then(data => setArticles(data))
//       .catch(error => setError(error));
//   }, []);

//   if (error) {
//     return <div>Error: {error.message}</div>;
//   }

//   return (
//     <div>
//       <h1>News Articles</h1>
//       <ul>
//         {articles.map((article, index) => (
//           <li key={index}>
//             <h2>{article.headline}</h2>
//             <a href={article.url} target="_blank" rel="noopener noreferrer">{article.url}</a>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default News;

import React, { useEffect, useState } from 'react';

function News() {
  const [articles, setArticles] = useState([]);
  const [error, setError] = useState(null);
  const [tickerString,setTickerString] = useState("TSLA,AAPL,MSFT")
  function Form(){
    const [inputValue, setInputValue] = useState("");

    function handleInputChange(event){
      setInputValue(event.target.value);
    }
    function handleSearch(event){
      event.preventDefault()
      setTickerString(inputValue)
      
    }
    return (
      <>
        <h1>Search Bar</h1>
        <form>
          <label htmlFor="tickers">Tickers (Enter as a comma-separated list): </label>
          <input
            type="text"
            id="tickers"
            placeholder="TSLA,AAPL,MSFT"
            value={inputValue}  // Bind input value to the state
            onChange={handleInputChange}  // Handle input changes
          />
          <button onClick={handleSearch}>Search</button>
        </form>
      </>
    );
  }
  useEffect(() => {
    const start = "2024-01-01";
    const end = "2024-08-30";
    //const tickerString = "TSLA"; // Example tickers
    
    // Helper function to get all months between start and end
    const getMonths = (startDate, endDate) => {
      const months = [];
      let currentDate = new Date(startDate);

      while (currentDate <= new Date(endDate)) {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth() + 1; // Month is 0-indexed
        const paddedMonth = month.toString().padStart(2, '0'); // Ensure 2-digit month format
        months.push(`${year}-${paddedMonth}`);
        currentDate.setMonth(currentDate.getMonth() + 1);
      }

      return months;
    };

    const months = getMonths(start, end);

    // Function to fetch data for each month and accumulate results
    const fetchMonthlyData = async () => {
      const allArticles = [];
      
      for (const month of months) {
        const monthStart = `${month}-01`;
        const monthEnd = new Date(new Date(monthStart).setMonth(new Date(monthStart).getMonth() + 1) - 1);
        const formattedMonthEnd = `${monthEnd.getFullYear()}-${(monthEnd.getMonth() + 1).toString().padStart(2, '0')}-${monthEnd.getDate().toString().padStart(2, '0')}`;

        try {
          const response = await fetch(`http://127.0.0.1:5000/api/news?tickers=${tickerString}&start=${monthStart}&end=${formattedMonthEnd}`);
          
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const data = await response.json();
          
          // Add the articles fetched for this month to the array of objects
          allArticles.push({
            month: month,
            articles: data,
          });
        } catch (error) {
          setError(error);
          console.error('Error fetching data:', error);
        }
      }

      // Set the final articles array to the state
      setArticles(allArticles); 
    };

    // Call the function to fetch articles for all months
    fetchMonthlyData();
  }, [tickerString]);

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
    <Form />
    <div>
      <h1>News Articles by Month</h1>
      {articles.map((monthData, index) => (
        <div key={index}>
          <h2>Articles for {monthData.month}</h2>
          <ul>
            {monthData.articles.map((article, i) => (
              <li key={i}>
                <h3>{article.headline}</h3>
                <a href={article.url} target="_blank" rel="noopener noreferrer">{article.url}</a>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
    </>
  );
}

export default News;
