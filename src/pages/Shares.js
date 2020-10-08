import React from 'react'

function Shares() {

  const [value, setValue] = useState(1)

  const renderOptions = () => {

  }

  const handleChange = async(event) => {
    setValue(event.target.value)
  }

  return (
    <>
    <div className='share container'>
      <form>
        <label>Select A trip to add members</label>
        <div className="share__select">
          <div className="share__selectDropdown">
            <select value={value} onChange={handleChange()}>
                {renderOptions()}
            </select>
          </div>
        </div>
      </form>
    </div>
    </>
  )
}

export default Shares;
