import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Person from './Person/Person';
import BasicTextFields from './Person/calendar'
import MultilineTextFields from './Person/selfInfo'
import LayoutTextFields from './Person/selfInfo_2'
import PrimarySearchAppBar from './Person/searchBar'
import MediaControlCard from './Person/imageMusic'

class App extends Component {
  state ={
    persons:[
      {name:'Max',age:'28'},
      {name:'May',age:'55'},
      {name:'Leo',age:'99'},
      ]
  };

  switchNameHandler = () => {
    //console.log("Was clicked.");
    this.setState(
      {
        persons:[
          {name:'Maxillium',age:'28'},
          {name:'May',age:'55'},
          {name:'Leo',age:'9'},
          ]
      }
    );

  }

//   render() {
//     return (
//       <div className="App">
//         <h1>處方系統</h1>
//         <button onClick = {this.switchNameHandler} >Switch Name</button>
//         < Person name ={this.state.persons[0].name} age={ this.state.persons[0].age}/>
//         < Person name ={ this.state.persons[1].name} age={ this.state.persons[1].age}/>
//         < Person name ={ this.state.persons[2].name} age={ this.state.persons[2].age}>My hobby is racing</Person>
//       </div>
//     );
//   }
// }
  
  render() {
    return (
      <div className="App">
        <h1>處方系統</h1>
        <PrimarySearchAppBar />
            <MediaControlCard />
        <BasicTextFields autoComplete="true"/>
        <MultilineTextFields />
        < Person />

        <LayoutTextFields/>

      </div>
    );
  }
}

export default App;
