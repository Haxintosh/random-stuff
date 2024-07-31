use regex::Regex;
use std::collections::{hash_map, HashMap};
use std::env;
use std::fs;

#[derive(Debug)]
struct Component {
    lcsc_id: String,
    mpn: String,
    manufacturer: String,
    package: String,
    category: ComponentTypes,
    value: String,
    data: HashMap<String, String>,
    qty: usize,
    price: f32,
}

#[derive(Debug)]
enum ComponentTypes {
    Capacitor,
    Resistor,
    Inductor,
    Diode,
    Transistor,
    VoltageRegulator,
    Transformer,
    Relay,
    LED,
    Potentiometer,
    Fuse,
    Connector,
    Crystal,
    Switch,
    Others,
}

pub(crate) fn main() {
    let file_path = "../LCSC.csv";

    let mut main_components_array: Vec<Component> = vec![];

    let contents = fs::read_to_string(file_path).expect("LCSC.csv");

    let mut reader = csv::Reader::from_reader(contents.as_bytes());
    for record in reader.records() {
        let record = record.unwrap();
        let mut data_hashmap = HashMap::new();
        data_hashmap.insert("original_data".to_string(), record[5].to_string());
        let mut component = Component {
            lcsc_id: record[0].to_string(),
            mpn: record[1].to_string(),
            manufacturer: record[2].to_string(),
            package: record[4].to_string(),
            category: ComponentTypes::Others,
            data: data_hashmap,
            qty: record[7].trim().parse::<usize>().unwrap(),
            value: "".to_string(),
            price: record[9].trim().parse::<f32>().unwrap(),
        };
        let data = record[5].to_string();
        match data {
            _ if data.contains("Capacitor") => component.category = ComponentTypes::Capacitor,
            _ if data.contains("Resistor") => component.category = ComponentTypes::Resistor,
            _ if data.contains("Inductor") => component.category = ComponentTypes::Inductor,
            _ if data.contains("Diode") => component.category = ComponentTypes::Diode,
            _ if data.contains("Transistor") => component.category = ComponentTypes::Transistor,
            _ if data.contains("LED") => component.category = ComponentTypes::LED,
            _ if data.contains("Connector") || data.contains("Headers") => {
                component.category = ComponentTypes::Connector
            }
            _ if data.contains("Fuse") => component.category = ComponentTypes::Fuse,
            _ if data.contains("Switch") => component.category = ComponentTypes::Switch,
            _ if data.contains("DC-DC Converter") => {
                component.category = ComponentTypes::VoltageRegulator
            }
            _ if data.contains("Crystals") => component.category = ComponentTypes::Crystal,

            _ => component.category = ComponentTypes::Others,
        }
        let data_parts: Vec<&str> = data.split(" ").collect::<Vec<&str>>();

        match component.category {
            ComponentTypes::Capacitor => {
                for (index, value) in data_parts.iter().enumerate() {
                    match index {
                        0 => {
                            component
                                .data
                                .insert("Voltage Rating".to_string(), value.to_string());
                        }
                        1 => {
                            // component
                            //     .data
                            //     .insert("Capacitance".to_string(), value.to_string());
                            component.value = value.to_string();
                        }
                        2 => {
                            component
                                .data
                                .insert("Dielectric".to_string(), value.to_string());
                        }
                        3 => {
                            component
                                .data
                                .insert("Tolerance".to_string(), value.to_string());
                        }
                        _ => {}
                    }
                }
            }
            ComponentTypes::Resistor => {
                let voltage_rating_regex = Regex::new(r"[0-9]+V|[0-9]+kV").unwrap();
                let temp_coeffiencient_regex = Regex::new(r"±[0-9]+ppm\/℃").unwrap();
                let tolerance_regex = Regex::new(r"±[0-9]+%").unwrap();
                let value_regex = Regex::new(r"[0-9]+\.*[0-9]+(p|n|u|μ|m|k|M|G|T)Ω").unwrap();

                let voltage_rating =
                    voltage_rating_regex.captures(&data).expect("Not found")[0].to_string();

                let temp_coefficient =
                    temp_coeffiencient_regex.captures(&data).expect("not found")[0].to_string();

                let tolerance = tolerance_regex.captures(&data).expect("not found")[0].to_string();

                let value = value_regex.captures(&data).expect("not found")[0].to_string();

                component
                    .data
                    .insert("Power Rating".to_string(), data_parts[0].to_string());

                component
                    .data
                    .insert("Voltage Rating".to_string(), voltage_rating.to_string());

                component.data.insert(
                    "Temp. Coeffiencient".to_string(),
                    temp_coefficient.to_string(),
                );

                component
                    .data
                    .insert("Tolerance".to_string(), tolerance.to_string());

                component.value = value;
            }

            _ => {}
        }

        println!("{:#?}", component);
    }
}
