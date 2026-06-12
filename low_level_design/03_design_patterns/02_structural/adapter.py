#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Structural)
Module: Adapter Pattern

The Adapter pattern allows objects with incompatible interfaces to collaborate.
It acts as a translator between a client and a service (Adaptee) that speaks
a different language.

Example:
An enterprise reporting dashboard expects user profile data in JSON format.
A legacy HR service provides data in XML format.
We implement an XML-to-JSON Adapter to reconcile them.
"""

import xml.etree.ElementTree as ET
import json

# =====================================================================
# THE CLIENT EXPECTATION (Target Interface)
# =====================================================================
class JSONTarget:
    """The client expects all data sources to output JSON string format."""
    def get_user_profile_json(self) -> str:
        pass


# =====================================================================
# THE LEGACY SERVICE (Adaptee)
# =====================================================================
class XMLAdaptee:
    """The existing service that returns data in XML format."""
    def get_user_profile_xml(self) -> str:
        return "<profile><id>101</id><name>Alice Smith</name><role>Architect</role></profile>"


# =====================================================================
# THE ADAPTER
# =====================================================================
class XMLToJSONAdapter(JSONTarget):
    """
    The Adapter implements the Target interface and delegates to the Adaptee,
    translating XML string output to a JSON string.
    """
    def __init__(self, xml_service: XMLAdaptee):
        self.xml_service = xml_service

    def get_user_profile_json(self) -> str:
        # Fetch raw XML from legacy service
        xml_data = self.xml_service.get_user_profile_xml()
        
        # Parse XML
        root = ET.fromstring(xml_data)
        user_id = root.find("id").text
        name = root.find("name").text
        role = root.find("role").text
        
        # Construct target JSON format
        profile_dict = {
            "userId": int(user_id),
            "fullName": name,
            "jobTitle": role
        }
        return json.dumps(profile_dict)


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("ADAPTER DESIGN PATTERN")
    print("==========================================================\n")

    # Legacy Service
    legacy_service = XMLAdaptee()
    print(f"Legacy Service Output (XML):\n  {legacy_service.get_user_profile_xml()}\n")

    # Adapter translation
    adapter = XMLToJSONAdapter(legacy_service)
    
    # Client consumption
    print("Client consuming translated data (JSON):")
    json_result = adapter.get_user_profile_json()
    print(f"  {json_result}")
    
    # Verify it is valid JSON
    parsed_json = json.loads(json_result)
    print(f"  Parsed values: UserID={parsed_json['userId']}, Name={parsed_json['fullName']}")

    print("\n==========================================================")
    print("Adapter Pattern module completed successfully!")
    print("==========================================================")
