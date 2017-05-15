import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'
import './App.css';
import io from 'socket.io-client';

const socket = io.connect();


class Match extends Component {
  constructor({match}) {
    super();
    this.state = {
    }
    fetch('/matches/' + match.params.matchId + '/')
      .then((response) => response.json())
      .then((tinderMatch) => this.setState({tinderMatch}));
  }

  render() {
    const match = this.state.tinderMatch;
    if (!match) {
      return null;
    }
    return (
      <div className="match">
        <Link to="/">Back</Link>
        <h1>{match.person.name}</h1>
        {match.person.photos.map((photo) => (
          <img
            src={photo.processedFiles[1].url}
            alt=""
            key={photo.id}
          />
        ))}

        <ul>
          {match.messages.map((message) => <li key={message._id}>{message.message}</li> )}
        </ul>
      </div>
    )
  }
}

const MatchItem = ({match}) => (
  <div className="match">
    <Link to={"/matches/" + match._id}>
      {match.person.name}<br/>
      <img src={match.person.photos[0].processedFiles[2].url} alt=""/>
    </Link>
  </div>
);

const MatchList = ({matches}) => (
  <div>
    {matches.map((match) => <MatchItem match={match} key={match._id} /> )}
  </div>
);

class Home extends Component {
  constructor() {
    super();
    this.state = {
      matches: []
    }
    fetch('/matches/')
      .then((response) => response.json())
      .then((matches) => this.setState({matches}));
  }

  render() {
    return (
      <MatchList matches={this.state.matches} />
    )
  }
}

const App = () => (
  <Router>
    <div>
      <Route exact path="/" component={Home} />
      <Route path="/matches/:matchId" component={Match} />
    </div>
  </Router>
);

export default App;
