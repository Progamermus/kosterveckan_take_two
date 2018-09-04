import React, { Component } from 'react';
import firebase from 'firebase';

class CreateEvent extends Component {

  constructor(props) {
    super(props);
    this.createEvent = this.createEvent.bind(this);
    this.randomIdGen = this.randomIdGen.bind(this);
  }

  randomIdGen () {
    return '/' + Math.random().toString(36).substr(2, 14);
  };

  createEvent() {
    var rootRef = firebase.database().ref('events');
    rootRef.push({eventURL: this.randomIdGen()})
  }

  render() {
    return (
      <div>
        <h1>
          Create event
        </h1>
        <button onClick={this.createEvent}>
          dont you dare push my button, hoe
        </button>
      </div>
    );
  }
}

export default CreateEvent;
