import { NavLink } from 'react-router-dom';

const Navbar = () => {
  const linkClass = ({ isActive }) =>
    isActive
      ? 'bg-blue-600 text-white hover:bg-blue-400 hover:text-white rounded-md px-3 py-2'
      : 'text-white hover:bg-blue-400 hover:text-white rounded-md px-3 py-2';

  return (
    <nav className='bg-rose-300'>
      <div className='mx-auto max-w-7xl px-2 sm:px-6 lg:px-8'>
        <div className='flex h-20 items-center justify-between'>
          <div className='flex flex-1 items-center justify-center md:items-stretch md:justify-start'>
            <NavLink className='flex flex-shrink-0 items-center mr-4' to='/'>
              <span className='hidden md:block text-white text-2xl font-bold ml-2'>
                React Jobs
              </span>
            </NavLink>
            <div className='md:ml-auto'>
              <div className='flex space-x-2'>
                <NavLink to='/' className={linkClass}>
                  Home
                </NavLink>
                <NavLink to='/previous-entries' className={linkClass}>
                  Previous Entries
                </NavLink>
                <NavLink to='/trends' className={linkClass}>
                  Trends
                </NavLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};
export default Navbar;