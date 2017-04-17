# Testing

> “Testing is an infinite process of comparing the invisible to the ambiguous in order to avoid the unthinkable
> happening to the anonymous.”— James Bach

## Unittests

We currently suck at this, but we accept PR's

## Integration Tests

We use postman collections and [Newman](https://www.getpostman.com/docs/newman_intro) for our integration testing.

### Executing Tests
Integration testing can be done by launching the docker-compose file located in the top
level of this repository, and then running the following commands from the tests directory

```
docker build -t collins-test
docker run -t -v $(pwd):/workspace collins-test
```