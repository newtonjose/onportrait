import React from "react";
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Button from '@material-ui/core/Button';
import SaveIcon from '@material-ui/icons/Save';


const styles = theme => ({
  container: {
    display: "flex",
    flexWrap: "wrap"
  },
  textField: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit
  },
  dense: {
    marginTop: 16
  },
  menu: {
    width: 200
  },

  button: {
    margin: theme.spacing.unit,
  },
  leftIcon: {
    marginRight: theme.spacing.unit,
  },
  rightIcon: {
    marginLeft: theme.spacing.unit,
  },
  iconSmall: {
    fontSize: 20,
  },
});

class FaceForm extends React.Component {
  handleChange = name => event => {
    this.setState({
      [name]: event.target.value
    });
  };

  render() {
    const { classes } = this.props;

    return (
      <form className={classes.container} noValidate autoComplete="off">
        <TextField
          required
          id="outlined-required"
          label="Name"
          className={classes.textField}
          onChange={this.handleChange("name")}
          margin="normal"
          variant="outlined"
        />

        <TextField
          required
          id="outlined-required"
          label="Instagram"
          defaultValue="@nickname"
          className={classes.textField}
          margin="normal"
          variant="outlined"
        />
        <Button variant="contained" size="small" className={classes.button}>
            <SaveIcon className={classNames(classes.leftIcon, classes.iconSmall)} />
            Save
        </Button>
      </form>
    );
  }
}

FaceForm.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(FaceForm);