import React, { Component } from 'react';
import SimpleAppBar from '../HomeBar';
import ImageNav from '../ImageNav';
import './Main.css'

class Main extends Component {
 render() {
   return (
       <dev>
           <SimpleAppBar></SimpleAppBar>
           <ImageNav className="Main"></ImageNav>
       </dev>
   );
 }
}

export default Main;