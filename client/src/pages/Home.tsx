import { Link } from "react-router-dom";

const Home = () => {
  const isLoggedIn = true;
  window.scrollTo(0,0);
  return (
    <div className="hero min-h-screen">
      <div className="hero-content text-center">
        <div className="max-w-md">
          <h1 className="text-6xl font-bold">uwplan</h1>
          <p className="py-6 text-2xl">
            Plan out your degree.
          </p>
          <button className="btn btn-secondary">
            {
              isLoggedIn ?
                <Link to="/me">Your Profile</Link>
              :
                <Link to="/login">Login</Link>
            }
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;
