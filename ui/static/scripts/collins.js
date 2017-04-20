// A view of the jobs screen
var JobsDashboard = React.createClass({
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
  // periodically update from API
  componentDidMount: function() {
      this.loadJobsFromAPI();
      setInterval(this.loadJobsFromAPI, this.props.pollInterval);
  },


 	render: function() {
 		return (
      <div className="ui-layout-center">
          <JobList data={this.state.data} />
      </div>

 		);
 	}
 });

// The list of rendered jobs
var JobList = React.createClass({
    render: function() {
        var ListEntries = this.props.data.map(function(job) {
            return (
                    <ListEntry name={job.name}
                               key={job.id}
                               every={job.interval.every}
                               period={job.interval.period}
                               enabled={job.enabled}
                               last_result ={job.last_result}>
                              //  {job.name}
                    </ListEntry>
            );
        });
        return (
            <div className="jobList">
            <table className="table table-hover table-striped">
                <thead>
                  <tr>
                    <th>Active</th>
                    <th>Job Name</th>
                    <th>Last Result</th>
                    <th>Frequency</th>
                  </tr>
                </thead>

             <tbody>

                {ListEntries}

            </tbody>
            </table>
            </div>
        );
    }
});

// a single list entry
var ListEntry = React.createClass({

    // returns class name based on whether the job is enabled or not
    setActiveClass: function(){

        if (this.props.enabled) {
            return "btn btn-success"
        } else  {
            return "btn btn-basic"
        }
    },
    // determines button color based on last result
    setLastResultClass: function(){
        if (this.props.last_result == "Passed") {
            return "btn btn-success"
        } else  {
            return "btn btn-danger"
        }
    },
    // change boolean to user friendly value
    label: function(){
        if (this.props.enabled) {
            return "Enabled"
        } else {
            return "Disabled"
        }
    },
    // HTML representation
    render: function() {
        return (
                <tr>
                  <td><button className={this.setActiveClass()}>{this.label()}</button></td>
                  <td>{this.props.name}</td>
                  <td><button className={this.setLastResultClass()}>{this.props.last_result}</button></td>
                  <td>{this.props.every} {this.props.period}</td>
                </tr>
        );
    }

});

var JobDetail = React.createClass({
  render: function() {
    return (
    <h1>Job Detail</h1>
    )
  }
}
)
