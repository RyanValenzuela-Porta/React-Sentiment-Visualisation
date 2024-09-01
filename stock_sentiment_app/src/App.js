

// import React, { useEffect, useState } from 'react';

// function News() {
//   // Move form states to the parent component
//   const [tickerString, setTickerString] = useState("TSLA,AAPL,MSFT");
//   const [startDate, setStartDate] = useState("2024-01-01");
//   const [endDate, setEndDate] = useState("2024-08-30");
//   const [inputValue, setInputValue] = useState(tickerString);
//   const [inputStart, setInputStart] = useState(startDate);
//   const [inputEnd, setInputEnd] = useState(endDate);

//   const [articles, setArticles] = useState([]);
//   const [error, setError] = useState(null);

//   // Handle form inputs and state changes
//   function handleInputChange(event) {
//     setInputValue(event.target.value);
//   }

//   function handleStartChange(event) {
//     setInputStart(event.target.value);
//   }

//   function handleEndChange(event) {
//     setInputEnd(event.target.value);
//   }

//   function handleSearch(event) {
//     event.preventDefault();
//     setTickerString(inputValue);
//     setStartDate(inputStart);
//     setEndDate(inputEnd);
//   }

//   // Fetch data when tickerString, startDate, or endDate changes
//   useEffect(() => {
//     const getMonths = (s, e) => {
//       const months = [];
//       let currentDate = new Date(s);

//       while (currentDate <= new Date(e)) {
//         const year = currentDate.getFullYear();
//         const month = currentDate.getMonth() + 1; // Month is 0-indexed
//         const paddedMonth = month.toString().padStart(2, '0'); // Ensure 2-digit month format
//         months.push(`${year}-${paddedMonth}`);
//         currentDate.setMonth(currentDate.getMonth() + 1);
//       }

//       return months;
//     };

//     const months = getMonths(startDate, endDate);

//     const fetchMonthlyData = async () => {
//       const allArticles = [];

//       for (const month of months) {
//         const monthStart = `${month}-01`;
//         const monthEnd = new Date(new Date(monthStart).setMonth(new Date(monthStart).getMonth() + 1) - 1);
//         const formattedMonthEnd = `${monthEnd.getFullYear()}-${(monthEnd.getMonth() + 1).toString().padStart(2, '0')}-${monthEnd.getDate().toString().padStart(2, '0')}`;

//         try {
//           const response = await fetch(`http://127.0.0.1:5000/api/news?tickers=${tickerString}&start=${monthStart}&end=${formattedMonthEnd}`);

//           if (!response.ok) {
//             throw new Error('Network response was not ok');
//           }

//           const data = await response.json();

//           // Add the articles fetched for this month to the array of objects
//           allArticles.push({
//             month: month,
//             articles: data,
//           });
//         } catch (error) {
//           setError(error);
//           console.error('Error fetching data:', error);
//         }
//       }

//       // Set the final articles array to the state
//       setArticles(allArticles);
//     };

//     // Call the function to fetch articles for all months
//     fetchMonthlyData();
//   }, [tickerString, startDate, endDate]);

//   if (error) {
//     return <div>Error: {error.message}</div>;
//   }

//   return (
//     <>
//       {/* Render Form */}
//       <div>
//         <h1>Search Bar</h1>
//         <form>
//           <label htmlFor="tickers">Tickers (Enter as a comma-separated list): </label>
//           <input
//             type="text"
//             id="tickers"
//             placeholder="TSLA,AAPL,MSFT"
//             value={inputValue}
//             onChange={handleInputChange}
//           />
//           <input
//             type="date"
//             id="start-date"
//             value={inputStart}
//             onChange={handleStartChange}
//           />
//           <input
//             type="date"
//             id="end-date"
//             value={inputEnd}
//             onChange={handleEndChange}
//           />
//           <button onClick={handleSearch}>Search</button>
//         </form>
//       </div>

//       {/* Render Articles */}
//       <div>
//         <h1>News Articles by Month</h1>
//         {articles.map((monthData, index) => (
//           <div key={index}>
//             <h2>Articles for {monthData.month}</h2>
//             <ul>
//               {monthData.articles.map((article, i) => (
//                 <li key={i}>
//                   <h3>{article.headline}</h3>
//                   <a href={article.url} target="_blank" rel="noopener noreferrer">{article.url}</a>
//                 </li>
//               ))}
//             </ul>
//           </div>
//         ))}
//       </div>
//     </>
//   );
// }

// export default News;
import React, { useEffect, useState } from 'react';

function News() {
  // Move form states to the parent component
  const [tickerString, setTickerString] = useState("TSLA,AAPL,MSFT");
  const [startDate, setStartDate] = useState("2024-01-01");
  const [endDate, setEndDate] = useState("2024-08-30");
  const [inputValue, setInputValue] = useState(tickerString);
  const [inputStart, setInputStart] = useState(startDate);
  const [inputEnd, setInputEnd] = useState(endDate);

  const [articles, setArticles] = useState([]);
  const [error, setError] = useState(null);

  // Handle form inputs and state changes
  function handleInputChange(event) {
    setInputValue(event.target.value);
  }

  function handleStartChange(event) {
    setInputStart(event.target.value);
  }

  function handleEndChange(event) {
    setInputEnd(event.target.value);
  }

  function handleSearch(event) {
    event.preventDefault();
    setTickerString(inputValue);
    setStartDate(inputStart);
    setEndDate(inputEnd);
  }

  // Use hardcoded data for now
  useEffect(() => {
    const getMonths = (s, e) => {
      const months = [];
      let currentDate = new Date(s);

      while (currentDate <= new Date(e)) {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth() + 1; // Month is 0-indexed
        const paddedMonth = month.toString().padStart(2, '0'); // Ensure 2-digit month format
        months.push(`${year}-${paddedMonth}`);
        currentDate.setMonth(currentDate.getMonth() + 1);
      }

      return months;
    };

    const months = getMonths(startDate, endDate);

    // Hardcoded data for testing
    const allArticles = months.map((month, index) => ({
      month: month,
      articles: [
        {
          headline: `Lorem Ipsum ${index + 1}`,
          url: "https://example.com/article-1"
        },
        {
          headline: `Dolor Sit Amet ${index + 1}`,
          url: "https://example.com/article-2"
        }
      ]
    }));

    // Simulate data fetching delay
    setTimeout(() => {
      setArticles(allArticles);
    }, 1000); // 1 second delay to simulate fetching

  }, [tickerString, startDate, endDate]);

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      {/* Render Form */}
      <div>
        <h1>Search Bar</h1>
        <form>
          <label htmlFor="tickers">Tickers (Enter as a comma-separated list): </label>
          <input
            type="text"
            id="tickers"
            placeholder="TSLA,AAPL,MSFT"
            value={inputValue}
            onChange={handleInputChange}
          />
          <input
            type="date"
            id="start-date"
            value={inputStart}
            onChange={handleStartChange}
          />
          <input
            type="date"
            id="end-date"
            value={inputEnd}
            onChange={handleEndChange}
          />
          <button onClick={handleSearch}>Search</button>
        </form>
      </div>

      {/* Render Articles */}
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
