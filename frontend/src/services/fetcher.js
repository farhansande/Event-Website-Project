export const fetcher = (url) => fetch(url).then((res) => res.json()); // takes the url,, calls fetch(url), wait for response, converts the response into json and returns the json
