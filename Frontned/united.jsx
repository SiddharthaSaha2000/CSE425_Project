import React, { useState, useEffect } from 'react';

const MyList = () => {
  const [doctors, setDoctors] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [filteredDoctors, setFilteredDoctors] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/doctor')
      .then((response) => response.json())
      .then((data) => {
        setDoctors(data.doctors);
        setFilteredDoctors(data.doctors);
      });
  }, []);

  const handleSearch = (e) => {
    const query = e.target.value;
    setSearchQuery(query);
    const filtered = doctors.filter((doctor) =>
    doctor.specialist.toLowerCase().includes(query.toLowerCase())
    );
    setFilteredDoctors(filtered);
  };

  return (
    <div>
      <center><h1 class="homeh"><i>Choose Your Doctor Wisely</i></h1></center>
      <br />
      <input
        type="text"
        value={searchQuery}
        onChange={handleSearch}
        placeholder="Search by Doctor's Speciality"
      />
      <ul className="doctor-list">
        {filteredDoctors.map((doctor) => (
          <li className="list" key={doctor.id}>
            <div>
              <img className='imguni'
                src={doctor.image_path}
                alt={doctor.name}
                width="150"
                height="200"
              />
              <h2 className='h2uni'>{doctor.name}</h2>
              <p className='puni'> {doctor.degree}</p>
              <p className='puniii'> <b>{doctor.specialist}</b></p>
              <p className='punii'>Hospital: <i><b> {doctor.hospital}</b></i></p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

function Lesgoo() {
  return (
    <>
      <div className="container">
        <MyList />
        <style>
          {`
            .lili {
              width: 25%;
              display: flex;
              align-items: center;
              margin-bottom: 20px;
            }

            h2 {
              margin: 0;
            }

            p {
              margin: 5px 0;
            }
          `}
        </style>
      </div>
    </>
  );
}

export default Lesgoo;