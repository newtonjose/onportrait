import React, { Component } from 'react';
import LaddaButton, { XL, EXPAND_RIGHT } from 'react-ladda';
import Pusher from 'pusher-js';
import './bar.css';

class Bar extends Component {
  state = {
    loading: false,
    progress: 0,
  };

  componentDidMount() {
    const pusher = new Pusher('<your app key>', {
      cluster: '<your app cluster>',
      encrypted: true,
    });

    const channel = pusher.subscribe('upload');
    channel.bind('progress', data => {
      this.setState({
        progress: data.percent / 100,
      });

      if (data.percent === 100) {
        this.setState({
          loading: false,
          progress: 0,
        });
      }
    });
  }

  handleClick = event => {
    event.preventDefault();

    this.setState({
      loading: !this.state.loading,
    });

    fetch('http://localhost:5000/api/upload', {
      method: 'POST',
    }).catch(error => console.log(error));
  };

  render() {
    const { loading, progress } = this.state;
    const message = loading ? (
      <span className="progress-text">{progress * 100}% completed</span>
    ) : null;

    return (
      <div className="Bar">
        <h1>Image Upload)</h1>
        <LaddaButton
          loading={this.state.loading}
          onClick={this.handleClick}
          progress={this.state.progress}
          data-color="#eee"
          data-size={XL}
          data-style={EXPAND_RIGHT}
          data-spinner-size={30}
          data-spinner-color="#ddd"
          data-spinner-lines={12}
        >
        </LaddaButton>

        {message}
      </div>
    );
  }
}

export default Bar;