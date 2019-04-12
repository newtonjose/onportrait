import React, { Component } from 'react';
import {Layer, Rect, Stage, Group} from 'react-konva';
import './FaceTagger.css'
import FaceRect from './Atons/FaceRect';
import FaceForm from './Atons/FaceForm';
import arnold from "../the_terminator_still.jpg";;


class TagImg extends Component {
  constructor(props){
    super(props);
    this.state={
      rects:[[100, 30, 70, 70], [40, 30, 70, 70]]
    };
    this.width = 400;
    this.height = 400;

    this.path = "../the_terminator_still.jpg";
  }

  render() {
       return (
        <div>
            <div className="Face-Tagger">
                <img src={arnold} alt="Logo" width="400" height="400"/>
                <div className="canvas">
                    <Stage width={this.width} height={this.height}>
                    <Layer>
                       <FaceRect/>
                    </Layer>
                    </Stage>
                    <FaceForm />
                </div>
            </div>

        </div>
        );
    }
}

export default TagImg;