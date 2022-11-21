import React from 'react';
import {Box, Flex} from '@chakra-ui/react';
import {BrowserRouter, Navigate, Route, Routes} from 'react-router-dom';
import {LoginProvider} from './components/LoginProvider';
import {Groups} from './components/Groups';
import GroupProfile from './components/GroupProfile';
import Navigation from './components/Navigation';
import Header from './components/Header';
import {FindGroupUp} from './components/FindGroupUp';
import AlertModal from './components/AlertModal';
import {GroupUps} from './components/GroupUps';
import GroupUpPage from './components/GroupUps/GroupUpPage';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <BrowserRouter>
      <Flex flex={1} direction={'column'} height="100%" maxW={'container.md'}>
        <Header />
        <LoginProvider>
          <Flex
            flex={1}
            direction={'column'}
            // height="100vh"
            bgColor="groupWhite.100"
            overflowY={'scroll'}
          >
            <Box flex={1} overflowY={'scroll'}>
              <Routes>
                {/* <Route path="/" element={<Temp>Home</Temp>} /> */}
                <Route path="/groups" element={<Groups />} />
                <Route path="/groups/:id" element={<GroupProfile />} />
                <Route path="/findgroupup" element={<FindGroupUp />} />
                <Route path="/groupups" element={<GroupUps />} />
                <Route path="/groupups/:id" element={<GroupUpPage />} />
                <Route path="/profile" element={<UserProfile />} />
                <Route path="*" element={<Navigate to={'/groupups'} />} />
              </Routes>
            </Box>
            <Navigation />
          </Flex>
        </LoginProvider>
        <AlertModal />
      </Flex>
    </BrowserRouter>
  );
}

export default App;
