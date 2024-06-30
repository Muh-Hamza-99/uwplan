const Footer = () => {
  return (
    <footer className="footer bg-neutral text-neutral-content items-center p-4">
      <aside className="grid-flow-col items-center">
        <h1 className="font-bold">uwplan</h1>
        <p>Copyright © 2024 - All right reserved</p>
      </aside>
      <nav className="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
        <a className="link link-hover">
          About
        </a>
        <a className="link link-hover">
          Instagram
        </a>
        <a className="link link-hover">
          LinkedIn
        </a>
      </nav>
    </footer>
  );
};

export default Footer;
