import React, { Component } from 'react';
import {Layer, Rect, Stage, Group} from 'react-konva';
import './FaceTagger.css'
import Image from '../ImageNav/Atons/Image';
import NameForm from './NameForm';
import arnold from "../ImageNav/Atons/the_terminator_still.jpg";;


class FaceTagger extends Component {
  constructor(props){
    super(props);
    this.state={
      styles: {},
    };
  }

  render() {
      this.items = this.props.facetagger.map((item, key) =>
          <div className="Face-Tagger" style={{top: item.x, left: item.y,}} >
            <canvas id="myCanvas" width={item.width} height={item.height}></canvas>
            <input type="text" className="Input-Tagger"/>
            <NameForm />
          </div>
      );
      return (
          <span>
              {this.items}
          </span>);
    }
}

export default FaceTagger;