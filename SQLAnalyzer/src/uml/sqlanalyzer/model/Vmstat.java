package sqlanalyzer.model;

import java.time.LocalDateTime;

public class Vmstat implements JsonModel {
 
	private LocalDateTime time;
	 
	private double us;
	 
	private double sy;
	 
	private double wa;
	 
	private double bi;
	 
	private double bo;
	 
	/**
	 * @see sqlanalyzer.model.JsonModel#toJson()
	 */
	public String toJson() {
		return null;
	}
	 
}
 
