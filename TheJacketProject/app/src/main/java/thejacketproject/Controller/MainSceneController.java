package thejacketproject.controller;

import thejacketproject.controller.FxmlFileLoader;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.util.Pair;

/**
 * The main page controller.
 */
public class MainSceneController {
  private Stage primaryStage;

  public void setPrimaryStage(Stage primaryStage) {
    this.primaryStage = primaryStage;
  }

  @FXML
  private Pane buttonPane;

  @FXML
  private Button closetButton;

  @FXML
  private Button homeButton;

  @FXML
  private AnchorPane mainAnchorPane;

  @FXML
    private BorderPane mainPane;

  @FXML
  private Pane standInPane;

  @FXML
  private Button userButton;

  @FXML
  void displayCloset(ActionEvent even) {

    FxmlFileLoader obj = new FxmlFileLoader();
    Pair<AnchorPane, Object> loaded = obj.getPane("Closet");

    ClosetController controller = (ClosetController) loaded.getValue();

    AnchorPane view = loaded.getKey();
    mainPane.setCenter(view);
  
  }

  @FXML
  void goHome(ActionEvent event) {

  }

  @FXML
  void showProfile(ActionEvent event) {

  }

  public void switchPane(Pane newPane) {
    
  }

}
