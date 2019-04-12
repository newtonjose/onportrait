import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from '@material-ui/core/Button';

const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  button: {
    margin: theme.spacing.unit,
  },
  input: {
    display: 'none',
  },
});


function HomeBar(props) {
  const { classes } = props;

  return (
    <div className={classes.root}>
      <AppBar position="static" color="default">
        <Toolbar>
          <Typography variant="h6" color="inherit">
            Online Portrait and Face Tagger
          </Typography>
          <div>
            <input
              accept="image/*"
              className={classes.input}
              id="outlined-button-file"
              multiple
              type="file"
            />
            <label htmlFor="outlined-button-file">
              <Button variant="outlined" component="span" className={classes.button}>
                Upload
              </Button>
            </label>
          </div>
        </Toolbar>
      </AppBar>
    </div>
  );
}

HomeBar.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(HomeBar);
