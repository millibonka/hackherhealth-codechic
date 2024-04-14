package thejacketproject.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

/**
 * COntrolls the home scene.
 */
public class HomeSceneController {
  private MainSceneController parent;
  private Stage primaryStage;

  public void setParent(MainSceneController parent) {
    this.parent = parent;
  }

  public void setPrimaryStage(Stage primaryStage) {
    this.primaryStage = primaryStage;
  }

  @FXML
  private Button getDressedButton;

  @FXML
  private Button headingOutButton;

  @FXML
  private Label locationLabel;

  @FXML
  private Label locationLabel1;

  @FXML
  private Button suggestedActivitiesButton;

  @FXML
  private Pane weatherConditionsPane;

  @FXML
  void exitList(ActionEvent event) {

  }

  @FXML
  void seeActivities(ActionEvent event) {

  }

  @FXML
  void seeClothes(ActionEvent event) {

  }

}
