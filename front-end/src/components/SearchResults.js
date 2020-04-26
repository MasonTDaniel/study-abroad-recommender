import React, { Component } from 'react'
import { Table } from 'reactstrap'

class SearchResults extends Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {

    }
    render() {
        // Make a table of programs and store it
        let filteredPrograms = this.props.state.filteredProgramList.map((program) => {
            return (
                <tr key={program.id}>
                    <td>{program.id}</td>
                    <td>{program.country}</td>
                    <td>{program.term}</td>
                    <td>{program.name}</td>
                    <td>{program.areaOfStudy}</td>
                    <td>{program.language}</td>
                    <td>{program.cost}</td>
                    <td><a href={program.website} target="_blank" rel="noopener noreferrer">{program.website}</a></td>
                </tr>
            )

        });
        if (Array.isArray(filteredPrograms) && filteredPrograms.length === 0) {
            return (
                <div>
                    <h5 style={{ "textAlign": "center" }}>No Results</h5>
                </div>
            )
        }
        return (
            <div className="result">
                <Table>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Country</th>
                            <th>Term</th>
                            <th>Name</th>
                            <th>Area of Study</th>
                            <th>Language</th>
                            <th>Cost</th>
                            <th>Website</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredPrograms}
                    </tbody>
                </Table>
            </div>
        )
    }
}

export default SearchResults;
