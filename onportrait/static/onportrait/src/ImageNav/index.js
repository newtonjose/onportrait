import React from 'react'
import axios, { post } from 'axios';
import arnold from "./Atons/the_terminator_still.jpg";
import Image from "./Atons/Image";
import Bar from './Atons/UploadBar'
import FaceTagger from "../FaceTagger";
import NameForm from '../FaceTagger/NameForm';
import LaddaButton, { XL, EXPAND_RIGHT } from 'react-ladda';

import './main.css'

class ImageNav extends React.Component {

  constructor(props) {
    super(props);
    this.state ={
      file:null,
      image: []
    };

    this.onFormSubmit = this.onFormSubmit.bind(this);
    this.onChange = this.onChange.bind(this);
    this.fileUpload = this.fileUpload.bind(this);
  }

  onFormSubmit(e){
    e.preventDefault() // Stop form submit
    this.fileUpload(this.state.file).then(response => {
      //console.debug()
      const image = response.data['data']['faces'];
      // console.log(image);
      this.setState({image});
    });
    this.image = (
        <div className="container">
            <Image/>
            <FaceTagger facetagger={this.state.image}></FaceTagger>
        </div>
    )
  }

  onChange(e) {
    this.setState({file:e.target.files[0]})
  }

  fileUpload(file){
    const url = 'http://0.0.0.0:5000/api/upload';
    const formData = new FormData();
    formData.append('file',file)
    const config = {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    }
    return  post(url, formData,config)
  }

  render() {
    return (
        <div>
        <form onSubmit={this.onFormSubmit}>
        <h1>File Upload</h1>
        <input type="file" onChange={this.onChange} />
        <button type="submit">Upload</button>
        </form>
      {this.image}
        </div>
   )
  }
}



export default ImageNav