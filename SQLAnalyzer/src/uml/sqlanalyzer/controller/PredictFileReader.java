package sqlanalyzer.controller;

import sqlanalyzer.model.PredictCollection;
import sqlanalyzer.model.JsonCollection;

public class PredictFileReader implements JsonReader {
 
	private PredictCollection predictCollection;
	 
	private JsonCollection jsonCollection;
	 
	/**
	 * @see sqlanalyzer.controller.JsonReader#readLines(java.lang.String[])
	 */
	public void readLines(String[] lines) {
	 
	}
	 
	/**
	 * @see sqlanalyzer.controller.JsonReader#getJson()
	 */
	public String getJson() {
		return null;
	}
	 
}
 
