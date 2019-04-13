import React from 'react';
import arnold from "./the_terminator_still.jpg";;

class Image extends React.Component {
    constructor(props) {
      super(props);
      this.state = { isMouseInside: false};
      this.handleMouseEnter = this.handleMouseEnter.bind(this);
      this.handleMouseLeave = this.handleMouseLeave.bind(this);

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
         <img src={arnold} alt="Logo" />
        );
    }
}

export default Image