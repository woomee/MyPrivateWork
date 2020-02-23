package sqlanalyzer.controller;

import sqlanalyzer.model.Vmstat;
import sqlanalyzer.model.JsonCollection;

public class StatFileReader implements JsonReader {
 
	private Vmstat vmstat;
	 
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
 
