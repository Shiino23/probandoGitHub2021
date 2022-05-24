import react, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import CarrouselImages from './Components/CarrouselImages';


function App() {
  const url = "https://api.themoviedb.org/3/movie/550?api_key=d48bcf2793cbc991ae82559e23c2ebe8&append_to_response=videos" 
  const fetchApi = async () => {
    const response = await fetch(url)
    console.log(response.data.results)
    
  }

  useEffect(() => {
  fetchApi()
  }, [])


  return (
    
    <CarrouselImages category= "Popular"/>
  );
}

export default App;
