import React, { Component } from 'react'
import { render } from 'react-dom'
//import {Row} from 'react-bootstrap'
import arnold from "../ImageNav/Atons/the_terminator_still.jpg";;

class TagImg extends Component {
  constructor(props){
    super(props);
    this.state={
      rects:[[110, 30, 70, 70], [40, 30, 70, 70]]
    };
    this.tagPerson = this.tagPerson.bind(this);
  }

  tagPerson(e){
    var x = e.offsetX,
        y = e.offsetY;

    for(var i=0;i<this.props.rects.length;i++) { // check whether:
        if(x > this.props.rects[i][0]            // mouse x between x and x + width
        && x < this.props.rects[i][0] + this.props.rects[i][2]
        && y > this.props.rects[i][1]            // mouse y between y and y + height
        && y < this.props.rects[i][1] + this.props.rects[i][3]) {
            alert('Rectangle ' + i + ' clicked');
        }
    }
  }

  drawRects() {
      const ctx = this.canvas.getContext('2d');
      ctx.drawImage(arnold, 0, 0, 300, 200);

      ctx.beginPath();
      ctx.strokeStyle="white";
      // for(var i=0;i<this.state.rects.length;i++) {
      //   // ctx.rect(this.state.rects[i][0], // fill at (x, y) with (width, height)
      //   //          this.state.rects[i][1],
      //   //          this.state.rects[i][2],
      //   //          this.state.rects[i][3]);
      //   console.log("helloo");
      // }
      console.log(this.state.rects);

      ctx.stroke();

  }

  componentDidMount() {
    console.log("componentDidMount");
    var myImage = new Image();
    myImage.onload = this.drawRects.bind(this);
    myImage.src = this.props.path;
  }
  render() {
    this.drawRects();
    return (
      <div>
      <form id="afterUpload" action="" method="post" encType="multipart/form-data">
        <div id="image_preview" className="row">
          <canvas ref="canvas" onClick={this.tagPerson}/>
        </div>
      </form>
      </div>
    );
  }
}

export default TagImg;