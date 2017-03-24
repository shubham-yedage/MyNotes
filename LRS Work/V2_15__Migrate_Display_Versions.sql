DELIMITER ;;
-- Add os_version and software_version data in device table from device_event table.
CREATE PROCEDURE addDeviceVersionInformation() BEGIN
  -- Update OS Version
  UPDATE device AS d, device_events AS de1 
    INNER JOIN (SELECT de.product_id, MAX(de.eventts) as latest_date_time from device_events de
      WHERE de.event_name IN ('FIRMWARE_VERSION', 'OS_VERSION') 
      GROUP BY de.product_id) AS de2
  ON de1.product_id = de2.product_id AND de1.eventts = de2.latest_date_time
    SET d.os_version = de1.event_data
    WHERE de1.event_name IN ('FIRMWARE_VERSION', 'OS_VERSION') 
    AND d.device_type = 'TABLE_TRACKER'
    AND d.id = de1.product_id;
    
  -- Update App version
  UPDATE device AS d, device_events AS de1 
    INNER JOIN (SELECT de.product_id, MAX(de.eventts) as latest_date_time from device_events de
      WHERE de.event_name IN ('APP_VERSION', 'WINTT_VERSION') 
      GROUP BY de.product_id) AS de2
  ON de1.product_id = de2.product_id AND de1.eventts = de2.latest_date_time
    SET d.software_version = de1.event_data
    WHERE de1.event_name IN ('APP_VERSION', 'WINTT_VERSION') 
    AND d.device_type = 'TABLE_TRACKER'
    AND d.id = de1.product_id;
    
END ;;
DELIMITER ;

call addDeviceVersionInformation();



DROP PROCEDURE IF EXISTS addDeviceVersionInformation;
