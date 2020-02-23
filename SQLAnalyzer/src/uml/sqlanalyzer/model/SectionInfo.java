package sqlanalyzer.model;

import java.time.LocalDateTime;

public class SectionInfo implements JsonModel {
 
	private int no;
	 
	private LocalDateTime start;
	 
	private int end:LocalDateTime;
	 
	private int scanRows;
	 
	/**
	 * @see sqlanalyzer.model.JsonModel#toJson()
	 */
	public String toJson() {
		return null;
	}
	 
}
 
