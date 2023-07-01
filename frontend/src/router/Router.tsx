import { Routes, Route } from 'react-router-dom';

import Books from '../pages/Books';

const Router = () => {
    return (         
        <Routes>
        <Route path='/' element={<Books/>} />
    </Routes>
    );
}
export default Router;