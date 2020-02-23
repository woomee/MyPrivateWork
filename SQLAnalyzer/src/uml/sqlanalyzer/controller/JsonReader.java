package sqlanalyzer.controller;

public interface JsonReader {
 
	public abstract void readLines(String[] lines);
	public abstract String getJson();
}
 
