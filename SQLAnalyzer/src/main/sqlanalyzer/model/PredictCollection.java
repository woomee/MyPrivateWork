package sqlanalyzer.model;

import java.util.List;

public class PredictCollection extends JsonCollection implements JsonModel {
 
	private List _predictList;
	 
	private Predict predict;
	 
	public double getSumReal() {
		return 0;
	}
	 
	public double getSumEst() {
		return 0;
	}
	 
	public double getErr() {
		return 0;
	}
	 
	/**
	 * @see sqlanalyzer.model.JsonModel#toJson()
	 */
	public String toJson() {
		return null;
	}
	 
}
 
