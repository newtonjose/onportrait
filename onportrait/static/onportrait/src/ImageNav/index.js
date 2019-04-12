import React, { Component } from 'react';
import logo from '../arnold.jpg'; // Tell Webpack this JS file uses this image
import FaceTagger from '../FaceTagger';
import TagImg from '../FaceTagger'
console.log(logo); // /logo.84287d09.png

class ImageNav extends Component {
  // Import result is the URL of your image
  render() {
    return (
    <div>
        <TagImg/>
    </div>
  );
  }
}

export default ImageNav;