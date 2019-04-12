import React from 'react';
import {Layer, Rect, Stage, Group} from 'react-konva';

class FaceRect extends React.Component {
    constructor(props) {
      super(props);
      this.state = { isMouseInside: false};
      this.handleMouseEnter = this.handleMouseEnter.bind(this);
      this.handleMouseLeave = this.handleMouseLeave.bind(this);

      this.positionX = 279;
      this.positionY = 69;
      this.width = 50;
      this.height = 50
    }

    handleMouseEnter() {
        this.setState({ isMouseInside: true});
    }
    handleMouseLeave() {
        this.setState({ isMouseInside: false});
    }

    render() {
        return (
            <Rect
                x={this.positionX} y={this.positionY} width={this.width} height={this.height}
                fill="" stroke="black"
                shadowBlur={10}
                strokeWidth={this.state.isMouseInside ? 3 : 1}
                onMouseEnter={this.handleMouseEnter}
                onMouseLeave={this.handleMouseLeave}
            />

        );
    }
}

export default FaceRect