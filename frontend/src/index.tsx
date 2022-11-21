import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {ChakraProvider, extendTheme} from '@chakra-ui/react';
import {RecoilRoot} from 'recoil';

const theme = extendTheme({
  colors: {
    groupGreen: '#024338',
    groupRed: '#9A2929',
    groupWhite: {
      100: '#F2F2F2', //grey background
      200: '#FCFCFC', //white
    },
    groupBlue: '#95BFFF',
    groupOrange: '#FF9960',
    groupGold: '#FFC107',
  },
});

ReactDOM.render(
  <React.StrictMode>
    <RecoilRoot>
      <ChakraProvider theme={theme}>
        <App />
      </ChakraProvider>
    </RecoilRoot>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
