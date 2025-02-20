import React from 'react'
import Snacks from './Snacks'
import Breakfast from './Breakfast'
import Cheat from './Cheat'
import Dinner from './Dinner'
import Lunch from './Lunch'



class DailyFoodLog extends React.Component {

    render()
    {
        return (
            <>
                <Breakfast />
                <Lunch />
                <Dinner />
                <Snacks />
                <Cheat />
            </>
        )
    }
}
export default DailyFoodLog