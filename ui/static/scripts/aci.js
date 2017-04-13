// An ACI fabric
var Jobs = React.createClass({displayName: 'Jobs',
    getInitialState: function() {
        return {data: []};
    },

    loadJobsFromAPI: function() {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    componentDidMount: function() {
        this.loadJobsFromAPI();
        setInterval(this.loadJobsFromAPI, this.props.pollInterval);
    },
    render: function() {
        return (
            <div className="jobs">
            <JobList data={this.state.data} />
        </div>
        )
    }
});

// A job list
var JobList = React.createClass({
    render: function() {
        var JobTiles = this.props.data.map(function(job) {
            return (
                <JobTile name={job.name}
            key={job.id}
            active={job.active}
            last_result ={job.last_result}>
            {job.name}

            </JobTile>
            );
        });
        return (
            <div className="jobList">
            {JobTiles}
            </div>
        );
    }
});


var JobTile = React.createClass({
    // returns class name based on whether the job is active or not
    setActiveClass: function(){
        console.log(this)
        if (this.props.active) {
            return "btn btn-success"
        } else  {
            return "btn btn-basic"
        }
    },
    setLastResultClass: function(){
        if (this.props.last_result == "Passed") {
            return "btn btn-success"
        } else  {
            return "btn btn-danger"
        }
    },
    label: function(){
        if (this.props.active) {
            return "Active"
        } else {
            return "Inactive"
        }
    },

    render: function() {
        return (
            // This is where we render the html representation of the object's icon
            // <div className="foo"> here will render as <div class="foo">
            // start as a simple list, comment this line out and add your code below

            // End html representation
            <div className="col-sm-4">
            <div className="tile gray">
            <h3 className="title">
            {this.props.name}
        </h3>
        <div className="faults">
            <div className="col-sm-4">
            <button className={this.setActiveClass()}>{this.label()}</button>

        </div>
        <div className="col-sm-4">
            <button className={this.setLastResultClass()}>{this.props.last_result}</button>

        </div>


        </div>
        </div>
        </div>
        // End html representation
        );
    }

});
