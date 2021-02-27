import React from 'react';



const  person = (props)=>{
    return (
      <div>
        <p> My name is {props.name} and I am {props.age} years old.</p>
        <p> {props.children}</p>
      </div>

    )
    
};

// import React from 'react';
// import Button from '@material-ui/core/Button';
// import 'date-fns';


// function person(){
//   return (
//     <Button variant="contained" color="primary">
//       提交資料
//     </Button>
//   );
// }



export default person;
