import React, { Component } from 'react';
import './App.css';

const Match = (match) => {
  return (
    <div key={match._id} className="match">
      <p>{match.person.name}</p>
      <img src={match.person.photos[0].processedFiles[3].url} alt=""/>
    </div>
  );
};

class Matches extends Component {
  constructor() {
    super()
    this.state = {
      matches: []
    }
    fetch('/matches/')
      .then((response) => response.json())
      .then((matches) => this.setState({matches}));
  }

  render() {
    return (
      <div>
        {this.state.matches.map((match) => {
          return Match(match);
        })}
      </div>
    );
  }
}

class App extends Component {
  render() {
    return <Matches />;
  }
}

export default App;
