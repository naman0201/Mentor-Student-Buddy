/* eslint-disable prettier/prettier */
/* eslint-disable react/prop-types */
import React, { Component, Suspense } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './scss/style.scss'
const loading = (
  <div className="pt-3 text-center">
    <div className="sk-spinner sk-spinner-pulse"></div>
  </div>
)

// Containers
const DefaultLayout = React.lazy(() => import('./layout/DefaultLayout'))


// Pages
const LandingPage = React.lazy(() => import('./views/pages/LandingPage/LandingPage'))
const Page404 = React.lazy(() => import('./views/pages/page404/Page404'))
const Page500 = React.lazy(() => import('./views/pages/page500/Page500'))

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Suspense fallback={loading}>
          <Routes>
            <Route index path="*" name="Home" element={<DefaultLayout />} />
            <Route exact path="/Home" name="Page 404" element={<DefaultLayout />}/>
            <Route exact path="/404" name="Page 404" element={<Page404 />} />
            <Route exact path="/500" name="Page 500" element={<Page500 />} />
            <Route exact path="/login" name="login"  element={<LandingPage />} />
            {/* <Route path="/loginpage" name="Login Page" element={<LoginPage />} /> */}
            {/* <Route exact path="/register" name="Register Page" element={<Register />} /> */}
          </Routes>
        </Suspense>
      </BrowserRouter>
    )
  }
}

export default App
