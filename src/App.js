import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import {useEffect, useState} from "react";

function App() {
    const [videos, setVideos] = useState([
        {name: "ale urwał", source: "/pitragoras_nauka.mp4", author: "szczecin", likes: 21, views: 47},
        {name: "xd1", source: "/dog.mp4", author: "debil", likes: 34, views: 156},
        {name: "skrót pluty", source: "/pitragoras_nauka.mp4", author: "podwale tv", likes: 456, views: 3456},
        {name: "dramat", source: "/pitragoras_nauka.mp4", author: "kibica robert", likes: 231, views: 477},
    ]);
    const [selectedVideo, setSelectedVideo] = useState(0);

  return (
      <>
          <div className="container">
              <div className="row">
                  <div className="col">
                      <video width="100%" src={videos[selectedVideo].source} controls/>
                      <h2>
                          {videos[selectedVideo].name}
                      </h2>
                      <p>
                          Dodany przez: {videos[selectedVideo].author}, polubień: {videos[selectedVideo].likes},
                          wyświetleń: {videos[selectedVideo].views}
                      </p>
                      <p>
                          {/*   To tutaj jest trochę do wykucia na pamięć żeby działało :( */}
                          <button type="button" className="btn btn-primary" onClick={() => {
                                  let newVideos = videos;              // tworzymy kopie tablicy
                                  newVideos[selectedVideo].likes += 1; // zwiększamy wartość którą chcemy zmienić
                                  setVideos([...newVideos]);
                                  // tutaj musi być takie coś [...newVideos] bo inaczej sie nie odświeży na stronie
                              }}>
                              Lubię to!
                          </button>
                      </p>

                  </div>
                  <div className="col">
                      <h2>
                          Zobacz też inne filmy
                      </h2>
                      <ul className="list-group">
                          {/* ten drugi argument w funkcji w mapie, index - działa jak indeks w pętli (jak w for (int i = 0... ) */}
                          {/* zlicza który z kolei element w tablicy obecnie obsługuje*/}
                          {videos.map((video, index) => (
                              <li className="list-group-item"
                                  key={index}
                                  onClick={() => {
                                      {/* i tutaj na przykład: w onClicku ustawia nam wideo na takie o indeksie jaki tu jest*/}
                                      {/* dla pierwszego elementu index to 0, dla drugiego 1, i tak dalej*/}
                                      setSelectedVideo(index);
                                      let newVideos = videos;
                                      newVideos[index].views += 1;
                                      setVideos([...newVideos]);
                              }}>
                                  {videos[index].name}
                              </li>
                          ))}
                      </ul>
                  </div>
              </div>
          </div>
      </>

  );
}

export default App;
