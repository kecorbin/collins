# Plugins


## Development

Some things to consider when developing a plugin.


##### Passing plugin data

All plugin data provided by the user will be accessible in the environment
your plugin executes, make sure and catch errors accessing these keys
and pass a suitable message back as the response indicating any data that
may have not been set correctly when the job was created.

##### Exit Code

Your plugin should always exit with code 0, even for failed jobs
, in this way, we can help the user identify whether the plugin failed
to execute, or whether the test/check actually failed.  We treat a
non 0 exit code as a failure of the plugin actually running.






