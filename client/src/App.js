import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'
import './App.css';

const MatchItem = ({match}) => (
  <div className="match">
    <Link to={"/matches/" + match._id}>{match.person.name}</Link><br/>
    <img src={match.person.photos[0].processedFiles[3].url} alt=""/>
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
    </div>
  </Router>
);

export default App;
