# Plugins


## Development

Some things to consider when developing a plugin.


##### Passing plugin data

All plugin data provided by the user will be accessible in the environment
your plugin executes, make sure and catch errors accessing these keys
and pass a suitable message back as the response indicating any data that
may have not been set correctly when the job was created.


##### Displaying Results

Your plugin can display information in plain HTML. Sample report:

```
  <img src="https://mycompany.com/logo">
  <br>
  <div style="text-align:center"><H1>Daily Summary from MyCompany</h1></div>
  <div class="content">
    <div class="table-responsive table-full-width">
      <table class="table table-hover table-striped">
        <thead>
          <tr>
            <th>Check</th>
            <th>Description</th>
            <th>Status</th>

          </tr>
        </thead>
        <tbody>
          <tr>
           <td>Ping</td>
           <td>verifies that all the monitored devices are pingable</td>
           <td>Passed</td>
         </tr>
         <tr>
          <td>Janus Gateway</td>
          <td>Verfies that janus is online and operating properly</td>
          <td>Passed</td>
        </tr>
        <tr>
         <td>Internet Speedy</td>
         <td>Verifies that internet speed is with 1 standard deviation</td>
         <td>Passed</td>
       </tr>
        </tbody>
      </table>
    </div>
  </div>

```
##### Exit Code

Your plugin should always exit with code 0, even for failed jobs
, in this way, we can help the user identify whether the plugin failed
to execute, or whether the test/check actually failed.  We treat a
non 0 exit code as a failure of the plugin actually running.






