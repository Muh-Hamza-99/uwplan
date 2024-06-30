import Term from "../components/Term";

const Me = () => {
  return (
    <div className="p-4">
        <div className="navbar bg-base-100">
          <div className="flex-1">
            <h1 className="text-2xl font-bold">Profile</h1>
          </div>
          <div className="flex-none">
            <button className="btn btn-secondary">Add Term</button>
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <Term termId={1} />
            <Term termId={2} />
            <Term termId={3} />
        </div>
    </div>
  );
};

export default Me;
