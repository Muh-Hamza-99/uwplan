import Term from "../components/Term";

const Me = () => {
  return (
    <div>
        <h1>Me</h1>
        <div className="p-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <Term />
            <Term />
            <Term />
        </div>
    </div>
  );
};

export default Me;
